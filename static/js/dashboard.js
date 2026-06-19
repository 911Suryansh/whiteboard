console.log("Dashboard JS LOADED");

let formType = "";

// =======================
// ELEMENT HELPERS
// =======================
function get(id) {
    return document.getElementById(id);
}

// =======================
// SHOW FORM (COMMON LOGIC)
// =======================
function showForm(type) {
    formType = type;

    const form = get("roomForm");
    const title = get("formTitle");
    const roomInput = get("roomInput");

    // show form (with new UI system)
    form.classList.remove("hidden");

    // reset fields
    get("username").value = "";
    roomInput.value = "";

    if (type === "create") {
        title.innerText = "Create Room";
        roomInput.placeholder = "Enter Room Name";
    } else {
        title.innerText = "Join Room";
        roomInput.placeholder = "Enter Room Code";
    }
}

// wrappers (keeps your HTML unchanged)
function showCreateForm() {
    showForm("create");
}

function showJoinForm() {
    showForm("join");
}

// =======================
// SUBMIT FORM
// =======================
function submitForm() {
    if (formType === "create") {
        createRoom();
    } else if (formType === "join") {
        joinRoom();
    }
}

// =======================
// CREATE ROOM
// =======================
async function createRoom() {

    const roomName = get("roomInput").value.trim();
    const username = get("username").value.trim();

    if (!roomName || !username) {
        alert("All fields are required");
        return;
    }

    localStorage.setItem("username", username);

    try {
        const res = await fetch("/api/rooms", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: roomName,
                username: username
            })
        });

        const data = await res.json();

        console.log("Create Room Response:", data);

        if (!res.ok || data.error) {
            alert(data.error || "Failed to create room");
            return;
        }

        alert(`Room Created!\nCode: ${data.room_code}`);

        // small UX delay for smoother transition
        setTimeout(() => {
            window.location.href = `/room/${data.room_id}`;
        }, 300);

    } catch (err) {
        console.error("Create Room Error:", err);
        alert("Error creating room. Please try again.");
    }
}

// =======================
// JOIN ROOM
// =======================
async function joinRoom() {

    const roomCode = get("roomInput").value.trim();
    const username = get("username").value.trim();

    if (!roomCode || !username) {
        alert("Room code and username are required");
        return;
    }

    localStorage.setItem("username", username);

    try {
        const res = await fetch("/api/rooms/join", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: roomCode,
                username: username
            })
        });

        const data = await res.json();

        console.log("Join Room Response:", data);

        if (!res.ok || data.error) {
            alert(data.error || "Failed to join room");
            return;
        }

        alert("Joined Room Successfully!");

        setTimeout(() => {
            window.location.href = `/room/${data.room_id}`;
        }, 300);

    } catch (err) {
        console.error("Join Room Error:", err);
        alert("Error joining room. Please try again.");
    }
}