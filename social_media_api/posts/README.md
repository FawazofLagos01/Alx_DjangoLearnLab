## Posts Endpoints
- GET /api/posts/
- POST /api/posts/
- GET /api/posts/{id}/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

## Comments Endpoints
- GET /api/comments/
- POST /api/comments/
- GET /api/comments/{id}/
- PUT /api/comments/{id}/
- DELETE /api/comments/{id}/

## Features
- Token Authentication
- Owner-based permissions
- Pagination
- Search filtering

## Follow / Unfollow Users

- **Follow**: POST /api/accounts/follow/<user_id>/
- **Unfollow**: POST /api/accounts/unfollow/<user_id>/

## Feed

- **Get Feed**: GET /api/feed/
- Returns posts from users the current user follows, most recent first.
