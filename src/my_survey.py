from flask_login import current_user
from hemlock import User, Page, utils
from hemlock.functional import compile, validate, test_response
from hemlock.questions import Check, Input, Label, Range, Select, Textarea
from sqlalchemy_mutable.utils import partial
from hemlock.utils.random import Assigner
from flask import url_for
from hemlock.utils.statics import make_figure


assigner = Assigner({'mood':('happy','sad'),'image':(0,1)})

@User.route("/survey")
def seed():
    assignment = assigner.assign_user()
    fig_0 = "https://imgs.xkcd.com/comics/election_commentary.png" if assignment['mood']=='happy' else url_for("static", filename="code_quality.png")
    return [
        Page(
            Label(
                make_figure(fig_0,figure_align="right",caption= "feel these feels pls")
            )
        ),
        Page(
            Label("does this make you sad?"),

            Input(
                make_figure("https://imgs.xkcd.com/comics/wanna_see_the_code.png",figure_align="center") if assignment['image'] else "DO NOT LOOK HERE"
            )
        ),
        Page(
            Label("goodbye")
        )
    ]