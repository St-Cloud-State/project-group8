function search_course() {
    const id = document.getElementById('Course_ID').value;

    fetch(`/api/Courses?Course_ID=${id}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            const name      = document.getElementById('Course_Name');
            const credits   = document.getElementById('Course_Number_Credits');
            const rubric    = document.getElementById('Course_Rubric');
            const number    = document.getElementById('Course_Number');

            name.value = data.Course_Name;
            credits.value = data.Course_Number_Credits;
            rubric.value = data.Course_Rubric;
            number.value = data.Course_Number;

            alert("Success! ID Was: " + data.Course_ID)
        }
        else {
            error_popup('Error searching for Course:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Course:', error)
    });
}

function delete_course() {

}

function modify_course() {

}

function add_course() {
    const name      = document.getElementById('Course_Name').value;
    const credits   = document.getElementById('Course_Number_Credits').value;
    const rubric    = document.getElementById('Course_Rubric').value;
    const number    = document.getElementById('Course_Number').value;

    const data = {
        Course_Name: name,
        Course_Number_Credits: credits,
        Course_Rubric: rubric,
        Course_Number: number
    };

    fetch('/api/Courses', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        console.log('ID Was: ', data.Course_ID);
        alert("Success! ID Was: " + data.Course_ID)
    })
    .catch(error => {
        error_popup('Error adding Course:', error)
    });
}

function get_all_Courses() {
    const id = "ALL"

    // Each one of these needs to check for empty values before moving on
    const name      = document.getElementById('Course_Name').value;
    const credits   = document.getElementById('Course_Number_Credits').value;
    const rubric    = document.getElementById('Course_Rubric').value;
    const number    = document.getElementById('Course_Number').value;
    // If the field is empty then it needs to be set to "NULL" so the python knows not to search with this parameter

    const queryParams = new URLSearchParams({
        Course_ID: id,
        Course_Name: name,
        Course_Number_Credits: credits,
        Course_Rubric: rubric,
        Course_Number: number
    }).toString();

    fetch(`/api/Courses?${queryParams}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            download_file(data.filename)
            alert("Success!")
        }
        else {
            error_popup('Error searching for Course:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Course:', error)
    });
}




function search_section() {

}

function delete_section() {

}

function modify_section() {

}

function add_section() {

}

function get_all_Sections() {

}




function search_student() {

}

function delete_student() {

}

function modify_student() {

}

function add_student() {

}

function get_all_Students() {

}




function search_registration() {

}

function delete_registration() {

}

function modify_registration() {

}

function add_registration() {

}

function get_all_Registrations() {

}





function download_file(filename) {
    fetch(`/download?filename=${filename}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'output.json';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error('Error:', error));
}

function error_popup(error_string, error_code) {
    console.error(error_string, error_code);
    alert("error" + error_string + error_code)
}

function showDiv() {
    var selectedOperation = document.getElementById("operations").value;
    var divs = ["Course", "Section", "Student", "Registration"];
    divs.forEach(function(div) {
        document.getElementById(div).style.display = "none";
    });
    document.getElementById(selectedOperation).style.display = "block";
}