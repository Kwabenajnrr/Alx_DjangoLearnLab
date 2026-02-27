# Social Media API

## Setup Instructions

1. **Install dependencies:**
   - `pip install django djangorestframework Pillow`

2. **Project Structure:**
   - Django project: `social_media_api`
   - App for user management: `accounts`

3. **Custom User Model:**
   - Extends `AbstractUser` with fields: `bio`, `profile_picture`, `followers` (ManyToMany).

4. **Authentication:**
   - Uses Django REST Framework Token Authentication.
   - Endpoints:
     - `/accounts/register/` — Register new user (returns token)
     - `/accounts/login/` — Login (returns token)
     - `/accounts/profile/` — View/update profile (requires authentication)

5. **Run Server:**
   - Navigate to `social_media_api` directory.
   - Run: `python manage.py runserver`

6. **Testing:**
   - Use Postman or similar tool to test registration and login endpoints.
   - Ensure token is returned and can be used for authenticated requests.

## User Model Overview
- `username`, `email`, `bio`, `profile_picture`, `followers`

## Token Authentication
- Add `Authorization: Token <token>` header to authenticated requests.

---

For more details, see code in `accounts/models.py`, `accounts/views.py`, and `accounts/serializers.py`.
