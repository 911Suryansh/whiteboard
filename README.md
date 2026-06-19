# 🎨 Collaborative Whiteboard System

A real-time collaborative whiteboard application that allows multiple users to create rooms, join shared workspaces, and draw together instantly. Built using Flask, Socket.IO, MySQL, HTML, CSS, and JavaScript.

---

## 🚀 Features

### ✅ Room Management

* Create collaboration rooms
* Join rooms using room codes
* Isolated room architecture
* Multiple concurrent rooms

### ✅ Real-Time Collaboration

* Live drawing synchronization
* Socket.IO based communication
* Instant stroke broadcasting
* Multi-user collaboration

### ✅ Whiteboard Tools

* Pen tool
* Eraser tool
* Clear board
* Canvas drawing support

### ✅ Board Persistence

* Save whiteboard state
* Load saved board data
* Store board data in MySQL

### ✅ Export Options

* Download board as PNG image
* Download board as JSON file

### ✅ Room Isolation

Each room maintains its own:

* Users
* Whiteboard state
* Drawing events

No cross-room interference occurs.

---

# 🏗️ Tech Stack

## Backend

* Flask
* Flask-SocketIO
* MySQL
* REST APIs

## Frontend

* HTML5
* CSS3
* JavaScript
* Canvas API

## Real-Time Communication

* WebSockets via Socket.IO

## Future Deployment

* Gunicorn
* Eventlet
* Nginx
* Docker
* MySQL Server

---

# 📂 Project Structure

```text
project/
│
├── app.py
│
├── config/
│   ├── db.py
│   └── extension.py
│
├── routes/
│   ├── room_routes.py
│   └── board_routes.py
│
├── templates/
│   ├── dashboard.html
│   └── room.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── dashboard.js
│       └── room.js
│
└── requirements.txt
```

---


# ⚡ Socket.IO Events

## join_room

Used when a user joins a collaboration room.

### Purpose

Connects a client to a specific room channel.

---

## draw_end

Triggered when a user finishes drawing a stroke.

### Purpose

Broadcasts completed drawing data to all room participants.

---

## clear_board

Triggered when the board is cleared.

### Purpose

Synchronizes board clearing across all connected users.



# 🎨 Whiteboard Features

### Drawing Tools

* Pen
* Eraser

### Board Controls

* Save Board
* Clear Board
* Download PNG
* Download JSON

### Collaboration

* Real-time drawing
* Room isolation
* Multi-user support

---

# 🔄 Collaboration Flow

```text
User Draws
     │
     ▼
Canvas Updates Locally
     │
     ▼
Socket Event Emitted
     │
     ▼
Flask SocketIO Server
     │
     ▼
Broadcast To Room
     │
     ▼
Connected Users Receive Event
     │
     ▼
Canvas Updates Instantly
```

---

# 📈 Current Progress

## Completed

* Room Creation
* Room Joining
* Room Codes
* Canvas Whiteboard
* Pen Tool
* Eraser Tool
* Save Board
* Load Board
* Download PNG
* Download JSON
* Flask Socket.IO Integration
* Real-Time Drawing
* Room Isolation

---

# 🚀 Upcoming Features (Phase 9)

## 1. User Presence System

Display active users in a room.

## 2. Live Cursor Tracking

Features:

* User cursors
* Usernames beside cursors
* Smooth movement

Inspired by:

* Figma
* Miro

---

## 3. Undo / Redo

Keyboard shortcuts:

```text
CTRL + Z → Undo
CTRL + Y → Redo
```

---

## 4. Real-Time Auto Save

Automatically save board state without user interaction.

---

## 5. Advanced Synchronization

New users instantly receive:

* Saved board
* Latest unsaved strokes

---

## 6. Room Members Panel

Display active room participants in a sidebar.

---

## 7. Shape Tools

Add support for:

* Rectangle
* Circle
* Line
* Text
* Sticky Notes

---

## 8. Advanced Toolbar

* Pen
* Eraser
* Undo
* Redo
* Save
* Clear
* Download PNG
* Download JSON

---

## 9. Security Improvements

### Rate Limiting

Prevent socket spam and abuse.

### Input Validation

Validate:

* Room codes
* Usernames
* Drawing payloads

### Room Authorization

Future support for:

* Private rooms
* Invite-only access



## 👨‍💻 Author

**Suryansh Saini**

Built using Flask, Socket.IO, MySQL, HTML, CSS, and JavaScript.
