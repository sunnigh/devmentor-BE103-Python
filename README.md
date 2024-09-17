整體業務流程
1.用戶註冊：用戶通過註冊頁面創建帳號，並完成電子郵件驗證。
2.用戶登入：用戶在登入頁面使用帳號和密碼登入，並獲取 accessToken。
3.瀏覽事件：登入成功後，用戶進入事件列表頁面，瀏覽所有事件，並可選擇訂閱或取消訂閱。
4.編輯事件：管理員或特定權限的用戶可以編輯事件的語言及內容，並將更新的資料保存至後端。
5.查看事件詳情：用戶點擊某個事件進入詳情頁面，查看訂閱者及其通知日誌，並可以手動觸發事件通知。


1. 登入頁面（front\login.html）
功能：用戶使用帳號和密碼進行登入。
邏輯：
1.用戶輸入帳號和密碼，點擊登入按鈕。
2.表單通過 axios 發送 POST 請求到後端 API 以驗證帳號和密碼。
3.如果驗證成功，系統會生成一個 accessToken 並將其存儲在瀏覽器的 localStorage 中，並跳轉至 event.html（事件列表頁面）。
4.如果驗證失敗，用戶將會看到錯誤提示。

2. 2.註冊頁面（front\register.html）
功能：用戶可以創建帳號並進行註冊。
邏輯：
1.用戶輸入基本註冊信息：用戶名、帳號、密碼、偏好語言、電子郵件。
2.點擊 "發送驗證碼" 按鈕後，系統會發送驗證碼到用戶的電子郵件。
3.用戶輸入驗證碼並進行驗證，通過驗證後註冊按鈕會被啟用。
4.註冊表單提交後，系統檢查帳號和密碼是否重複，如果無誤則向後端發送註冊請求並創建新帳號。
5.註冊成功後，會自動跳轉到登入頁面。

3. 事件列表頁面（front\event.html）
功能：顯示所有的事件列表，並提供訂閱/取消訂閱和編輯事件的功能。
邏輯：
1.當用戶訪問此頁面時，系統會通過 accessToken 從後端獲取所有事件的列表，並動態渲染在表格中。
2.每個事件有多個操作選項：
3.訂閱/取消訂閱：點擊按鈕即可訂閱或取消訂閱該事件。訂閱信息會保存在 localStorage 中。
4.編輯事件內容：用戶可以編輯事件的語言和內容資料，編輯後數據會發送至後端更新。
5.點擊 "新增" 按鈕，可以新增一個新的事件及其內容。

4. 4.事件詳情頁面（front\event_detail.html）
功能：顯示特定事件的詳情和發送日誌。
邏輯：
1.當用戶訪問此頁面時，系統會根據事件 ID 從後端獲取該事件的詳細信息，包括所有訂閱該事件的用戶和發送日誌。
2.日誌會顯示每個用戶的通知方式、通知日期以及事件內容。
3.用戶可以點擊 "Trigger" 按鈕來觸發通知，通知會發送給所有已訂閱該事件的用戶。

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
