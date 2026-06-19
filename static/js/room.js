const socket = io();

const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");

let isDrawing = false;
let tool = "pen";

let boardData = [];
let currentStroke = [];

// ======================
// CANVAS SIZE FIX
// ======================
function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}

window.addEventListener("resize", resizeCanvas);
resizeCanvas();

// ======================
// INIT (FIXED)
// ======================
window.onload = async () => {

    let username = localStorage.getItem("username");

    console.log("Stored username:", username);

    if (!username || username === "null") {
        username = prompt("Enter your name:");

        if (!username) {
            username = "Anonymous";
        }

        localStorage.setItem("username", username);
    }

    console.log("Joining with username:", username);

    socket.emit("join_room", {
        room_id: roomId,
        username: username
    });

    await loadBoard();
};

// ======================
// TOOL
// ======================
function setTool(selectedTool) {
    tool = selectedTool;
}

// ======================
// DRAW START
// ======================
canvas.addEventListener("mousedown", (e) => {

    isDrawing = true;

    ctx.beginPath();

    const x = e.offsetX;
    const y = e.offsetY;

    currentStroke = [{ x, y }];

    ctx.moveTo(x, y);
});

// ======================
// DRAW MOVE
// ======================
canvas.addEventListener("mousemove", (e) => {

    if (!isDrawing) return;

    const x = e.offsetX;
    const y = e.offsetY;

    currentStroke.push({ x, y });

    ctx.lineCap = "round";

    if (tool === "pen") {
        ctx.strokeStyle = "black";
        ctx.lineWidth = 2;
    } else {
        ctx.strokeStyle = "white";
        ctx.lineWidth = 10;
    }

    ctx.lineTo(x, y);
    ctx.stroke();
});

// ======================
// DRAW END
// ======================
canvas.addEventListener("mouseup", () => {

    isDrawing = false;

    ctx.beginPath();

    boardData.push({
        tool,
        stroke: currentStroke
    });

    socket.emit("draw_end", {
        room_id: roomId,
        tool,
        stroke: currentStroke
    });
});

// ======================
// RECEIVE DRAW
// ======================
socket.on("draw_end", (data) => {

    const stroke = data.stroke;

    ctx.beginPath();

    stroke.forEach((p, i) => {
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
    });

    ctx.strokeStyle = data.tool === "eraser" ? "white" : "black";
    ctx.lineWidth = data.tool === "eraser" ? 10 : 2;

    ctx.stroke();
});

// ======================
// ROOM USERS (FIX NULL DISPLAY)
// ======================
socket.on("room_users", (users) => {

    const userList = document.getElementById("userList");

    if (!userList) return;

    userList.innerHTML = "";

    users.forEach(user => {

        const li = document.createElement("li");

        li.textContent = "🟢 " + (user || "Anonymous");

        userList.appendChild(li);
    });
});

// ======================
// USER JOIN / LEAVE DEBUG
// ======================
socket.on("user_joined", (data) => {
    console.log("JOIN:", data.username);
});

socket.on("user_left", (data) => {
    console.log("LEFT:", data.username);
});

// ======================
// CLEAR
// ======================
socket.on("clear_board", () => {

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    boardData = [];
});

function clearCanvas() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    boardData = [];

    socket.emit("clear_board", {
        room_id: roomId
    });
}

// ======================
// LOAD BOARD
// ======================
async function loadBoard() {

    const res = await fetch(`/api/rooms/${roomId}/board`);

    const data = await res.json();

    boardData = data.board ? JSON.parse(data.board) : [];

    redraw();
}

// ======================
// REDRAW
// ======================
function redraw() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    boardData.forEach(action => {

        ctx.beginPath();

        action.stroke.forEach((p, i) => {
            if (i === 0) ctx.moveTo(p.x, p.y);
            else ctx.lineTo(p.x, p.y);
        });

        ctx.strokeStyle = action.tool === "eraser" ? "white" : "black";
        ctx.lineWidth = action.tool === "eraser" ? 10 : 2;

        ctx.stroke();
    });
}

// ======================
// SAVE
// ======================
async function saveBoard() {

    const res = await fetch(`/api/rooms/${roomId}/board`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            board: JSON.stringify(boardData)
        })
    });

    const data = await res.json();

    alert(data.message);
}

// ======================
// DOWNLOAD PNG
// ======================
function downloadPNG() {

    const link = document.createElement("a");

    link.download = "whiteboard.png";
    link.href = canvas.toDataURL("image/png");

    link.click();
}

// ======================
// DOWNLOAD JSON
// ======================
function downloadJSON() {

    const blob = new Blob(
        [JSON.stringify(boardData)],
        { type: "application/json" }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "board.json";

    a.click();
}