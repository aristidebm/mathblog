import re

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from mathblog import db
from mathblog.models import User

PASSWORD_REGEX = re.compile(r"(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w@#$]{8,}")


class LoginForm(FlaskForm):
    # TODO : allow email or username, since both identify a user.
    email = StringField(
        "Email",
        validators=[Email(), DataRequired()],
        render_kw={"placeholder": "Email or Username"},
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    # TODO : username must not be required, generate one from email if the user doesn't provide one.
    username = StringField(
        "Username", validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )
    email = StringField(
        "Email",
        validators=[Email(), DataRequired()],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Confirm Password"},
    )
    submit = SubmitField("Register")

    @staticmethod
    def validate_password(form, field):
        # The password must contains a least:
        # + one special character: !,#,$,%,&,+,*,-,.,/,:,; <,=,>,?, [, \, ],^,_,`,{,|,},~,@,(,)
        # + one uppercase character [A-Z].
        # + one number [0-9]
        # + lowercase letter[a-z]
        # + the minimum length of 8.
        if not PASSWORD_REGEX.match(field.data):
            raise ValidationError(
                """
The password must contain at least one special character @#$,
one lower case, one upper case, one integer and be at least 8 character long.
            """
            )

    @staticmethod
    def validate_username(form, field):
        """
        check if the username is already taken by another
        user.
        """
        if db.session.query(
            User.query.filter_by(username=field.data).exists()
        ).scalar():
            raise ValidationError(
                "This username is already taken, please choose another one."
            )
