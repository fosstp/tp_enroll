from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    from pyramid_sqlalchemy import Session
    from ..models import NewComerModel

    new_comers = Session.query(NewComerModel).order_by(NewComerModel.signup_number)
    return {'new_comers': new_comers}

@view_config(route_name='signup_detail', renderer='templates/signup_detail.jinja2')
def signup_detail_view(request):
    from pyramid_sqlalchemy import Session
    from ..models import NewComerModel

    new_comers = Session.query(NewComerModel).filter_by(status=1).order_by(NewComerModel.signup_number)
    return {'new_comers': new_comers}
