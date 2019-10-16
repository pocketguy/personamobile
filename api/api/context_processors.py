from django.conf import settings


def site_name_processor(request):
    my_dict = {"site_url": settings.SITE_URL}

    return my_dict
