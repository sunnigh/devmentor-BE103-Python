# Installation && Setup
1. Clone the repository and into to directory.
    ```
    git clone git@github.com:jonyig/devmentor-BE103-Python.git && cd devmentor-BE103-Python
    ```

2. Start the container.
   ```sh
   docker-compose up -d 
   ```

3. Check API document
    ```
   localhots:8000
   ```


# Migration
- Upgrade
   ```
   alembic upgrade head      
   ```

- Downgrade
  ```
   alembic downgrade -1
   ```
  
- Current version
  ```
   alembic current 
   ```
  
- Current version
  ```
   alembic current 
   ```
  
- Create new migration
  ```
   alembic revision -m "create XXX table" 
   ```
  
# Example API

## List Post
```
curl --location '127.0.0.1:8080/posts'
```

## Create Post
```
curl --location '127.0.0.1:8080/posts' \
--header 'Content-Type: application/json' \
--data '{
    "title":"12344rr",
    "content" : "1333"
}'
```