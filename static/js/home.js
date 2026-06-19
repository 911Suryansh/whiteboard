function goToDashboard() {
    window.location.href = "/dashboard";
}

document
    .getElementById("heroBtn")
    .addEventListener("click", goToDashboard);

document
    .getElementById("navBtn")
    .addEventListener("click", goToDashboard);

document
    .getElementById("ctaBtn")
    .addEventListener("click", goToDashboard);