=====
Plans
=====

A ``Version`` has many ``Plans``, which detail the concrete steps to go
through to apply metadata to an org. Put another way, a ``Plan`` is like
a particular set of options for the ``Version``.

List
----

.. sourcecode:: http

   GET /api/plans/ HTTP/1.1

.. sourcecode:: http

   HTTP/1.1 200 OK

   [
     {
       "id": "g45z7wA",
       "title": "Full Install",
       "version": "XG4pVvD",
       "preflight_message": "<p>Preflight message</p>",
       "tier": "primary",
       "slug": "full-install",
       "old_slugs": [],
       "steps": [],
       "is_allowed": true,
       "is_listed": true,
       "not_allowed_instructions": null,
       "requires_preflight": true
     },
     ...
   ]

Retrieve
--------

.. sourcecode:: http
   
   GET /api/plans/g45z7wA/ HTTP/1.1

.. sourcecode:: http

   HTTP/1.1 200 OK

   {
     "id": "g45z7wA",
     "title": "Full Install",
     "version": "XG4pVvD",
     "preflight_message": "<p>Preflight message</p>",
     "tier": "primary",
     "slug": "full-install",
     "old_slugs": [],
     "steps": [],
     "is_allowed": true,
     "is_listed": true,
     "not_allowed_instructions": null,
     "requires_preflight": true
   }

Create
------

.. sourcecode:: http
   
   POST /api/plans/ HTTP/1.1

   {
     "title": "Full Install",
     "version": "XG4pVvD",
     "preflight_message": "<p>Preflight message</p>",
     "tier": "primary",
     "steps": [],
     "is_allowed": true,
     "is_listed": true,
     "not_allowed_instructions": null,
     "requires_preflight": true
   }

.. sourcecode:: http

   HTTP/1.1 201 CREATED

Update
------

.. sourcecode:: http
   
   PATCH /api/plans/g45z7wA/ HTTP/1.1

   {
     "preflight_message": "Oh *no*.",
   }

.. sourcecode:: http

   HTTP/1.1 200 OK

   {
     "id": "g45z7wA",
     "title": "Full Install",
     "version": "XG4pVvD",
     "preflight_message": "<p>Oh <strong>no</strong>.</p>",
     "tier": "primary",
     "slug": "full-install",
     "old_slugs": [],
     "steps": [],
     "is_allowed": true,
     "is_listed": true,
     "not_allowed_instructions": null,
     "requires_preflight": true
   }

Destroy
-------

.. sourcecode:: http
   
   DELETE /api/plans/g45z7wA/ HTTP/1.1

.. sourcecode:: http

   HTTP/1.1 204 NO CONTENT

Preflight Create
----------------

.. sourcecode:: http
   
   POST /api/plans/g45z7wA/preflight/ HTTP/1.1

.. sourcecode:: http

   HTTP/1.1 201 CREATED

Preflight Get
-------------

.. sourcecode:: http
   
   GET /api/plans/g45z7wA/preflight/ HTTP/1.1

.. sourcecode:: http

   HTTP/1.1 200 OK

   {
     "id": "107",
     "organization_url": "https://foo.salesforce.com",
     "user": "3Lw7OwK",
     "plan": "olNjglg",
     "created_at": "2019-05-03T18:30:18.240128Z",
     "edited_at": "2019-05-03T18:30:22.133936Z",
     "is_valid": true,
     "status": "complete",
     "results": {},
     "error_count": 0,
     "warning_count": 0,
     "is_ready": true
   }
