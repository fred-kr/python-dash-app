// Variables to store the initial position and size
let initX, initY, initW, initH, corner;

// Get the resize handles and container
const resizeHandleTopLeft = document.querySelector(".resize-handle-top-left");
const resizeHandleTopRight = document.querySelector(".resize-handle-top-right");
const resizeHandleBottomLeft = document.querySelector(".resize-handle-bottom-left");
const resizeHandleBottomRight = document.querySelector(".resize-handle-bottom-right");
const container = document.querySelector(".resize-container");
const style = window.getComputedStyle(container);

// Add event listeners for each corner
resizeHandleTopLeft.addEventListener("mousedown", onMouseDown);
resizeHandleTopRight.addEventListener("mousedown", onMouseDown);
resizeHandleBottomLeft.addEventListener("mousedown", onMouseDown);
resizeHandleBottomRight.addEventListener("mousedown", onMouseDown);

function onMouseDown(e) {
    e.preventDefault();

    // Store the initial position of the mouse and the container
    initX = e.clientX;
    initY = e.clientY;
    initW = parseInt(style.getPropertyValue("width"));
    initH = parseInt(style.getPropertyValue("height"));

    // Determine which corner is being dragged
    if (e.target === resizeHandleTopLeft) {
        corner = "top-left";
    } else if (e.target === resizeHandleTopRight) {
        corner = "top-right";
    } else if (e.target === resizeHandleBottomLeft) {
        corner = "bottom-left";
    } else if (e.target === resizeHandleBottomRight) {
        corner = "bottom-right";
    }

    // Add the event listeners for mouse move and mouse up
    window.addEventListener("mousemove", onMouseMove);
    window.addEventListener("mouseup", onMouseUp);
}

function onMouseMove(e) {
    e.preventDefault();

    const dx = e.clientX - initX;
    const dy = e.clientY - initY;

    if (corner === "top-left") {
        container.style.width = `${initW - dx}px`;
        container.style.height = `${initH - dy}px`;
    } else if (corner === "top-right") {
        container.style.width = `${initW + dx}px`;
        container.style.height = `${initH - dy}px`;
    } else if (corner === "bottom-left") {
        container.style.width = `${initW - dx}px`;
        container.style.height = `${initH + dy}px`;
    } else if (corner === "bottom-right") {
        container.style.width = `${initW + dx}px`;
        container.style.height = `${initH + dy}px`;
    }
}

function onMouseUp(e) {
    e.preventDefault();

    // Remove the event listeners for mouse move and mouse up
    window.removeEventListener("mousemove", onMouseMove);
    window.removeEventListener("mouseup", onMouseUp);
}
