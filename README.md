# GameVault API

REST API for managing video game reviews, wishlists, and ratings.

## Live API
https://gamevault-production-d21a.up.railway.app/api/games/

## Documentation
https://gamevault-production-d21a.up.railway.app/api/docs/

## Tech Stack
- Python / Django
- Django REST Framework
- JWT Authentication
- PostgreSQL (production)
- Railway (deployment)

## Endpoints
- `POST /api/register/` — Register user
- `POST /api/token/` — Login (get JWT tokens)
- `POST /api/token/refresh/` — Refresh token
- `GET/POST /api/games/` — List / create games
- `GET/POST /api/reviews/` — List / create reviews
- `GET/POST /api/wishlist/` — List / manage wishlist

## Features
- JWT authentication
- Role-based permissions
- Search and filtering
- Pagination
- Swagger documentation