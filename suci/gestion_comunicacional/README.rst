============
gestion_comunicacional
============

A Django application to record web-based communication management processes in SUCI Ven911.

- Social media registration
- Registration of assigned equipment
- Social Articulation

Quick start
-----------

1. Add "gestion_comunicacional" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "gestion_comunicacional",
    ]

2. Include the gestion_comunicacional URLconf in your project urls.py like this::

    path("gestion_comunicacional/", include("gestion_comunicacional.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a gestion_comunicacional

5. Visit the ``/gestion_comunicacional/`` URL to participate in the gestion_comunicacional