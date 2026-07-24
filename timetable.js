const TIMETABLE_API = "/api/timetable";

// Load timetable on page load
window.onload = function () {
    loadTimetable();
};

// -----------------------------
// Generate Timetable
// -----------------------------
async function generateTimetable() {

    const response = await fetch("/api/timetable/generate", {
        method: "POST"
    });

    if (response.ok) {
        alert("Timetable Generated Successfully");
        loadTimetable();
    } else {
        alert("Unable to Generate Timetable");
    }
}

// -----------------------------
// Load Timetable
// -----------------------------
async function loadTimetable() {

    const response = await fetch(TIMETABLE_API);
    const data = await response.json();

    let html = "";

    data.forEach(t => {

        html += `
        <tr>
            <td>${t.day}</td>
            <td>${t.slot}</td>
            <td>${t.division}</td>
            <td>${t.subject}</td>
            <td>${t.faculty}</td>
            <td>${t.room}</td>
            <td>${t.session_type}</td>
        </tr>
        `;

    });

    document.getElementById("timetableTable").innerHTML = html;
}
