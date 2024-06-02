============
gestion-comunicacional
============

A Django application to record web-based communication management processes in SUCI Ven911.

- Social media registration
- Registration of assigned equipment
- Social Articulation

Quick start
-----------

1. Add "gestion-comunicacional" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "gestion-comunicacional",
    ]

2. Include the gestion-comunicacional URLconf in your project urls.py like this::

    path("gestion-comunicacional/", include("gestion-comunicacional.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a gestion-comunicacional

5. Visit the ``/gestion-comunicacional/`` URL to participate in the gestion-comunicacional