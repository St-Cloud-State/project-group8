function search_course() {
    const id = document.getElementById('Course_ID').value;

    fetch(`/api/get/Courses?Course_ID=${id}`, {
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

    fetch('/api/post/Courses', {
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
    let name      = document.getElementById('Course_Name').value;
    let credits   = document.getElementById('Course_Number_Credits').value;
    let rubric    = document.getElementById('Course_Rubric').value;
    let number    = document.getElementById('Course_Number').value;

    name    = name.trim()       === "" ? "NULL":name   
    credits = credits.trim()    === "" ? "NULL":credits
    rubric  = rubric.trim()     === "" ? "NULL":rubric 
    number  = number.trim()     === "" ? "NULL":number 

    const queryParams = new URLSearchParams({
        Course_ID: "NULL",
        Course_Name: name,
        Course_Number_Credits: credits,
        Course_Rubric: rubric,
        Course_Number: number
    }).toString();

    fetch(`/api/get/Courses?${queryParams}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            if (data.filename) {
                download_file(data.filename)
                alert("Success!")
            }
            else {
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
    const id = document.getElementById('Section_ID').value;

    fetch(`/api/get/Sections?Section_ID=${id}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            const semester    = document.getElementById('Section_Semester');
            const course      = document.getElementById('Section_Course_ID');
            const schedule    = document.getElementById('Section_Schedule');
            const instructor  = document.getElementById('Section_Instructor');

            semester.value = data.Section_Semester;
            course.value = data.Section_Course_ID;
            schedule.value = data.Section_Schedule;
            instructor.value = data.Section_Instructor;

            alert("Success! ID Was: " + data.Section_ID)
        }
        else {
            error_popup('Error searching for Section:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Section:', error)
    });
}

function delete_section() {

}

function modify_section() {

}

function add_section() {
    const semester    = document.getElementById('Section_Semester').value;
    const course      = document.getElementById('Section_Course_ID').value;
    const schedule    = document.getElementById('Section_Schedule').value;
    const instructor  = document.getElementById('Section_Instructor').value;

    const data = {
        Section_Semester: semester,
        Section_Course_ID: course,
        Section_Schedule: schedule,
        Section_Instructor: instructor
    };

    fetch('/api/post/Sections', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        console.log('ID Was: ', data.Section_ID);
        alert("Success! ID Was: " + data.Section_ID)
    })
    .catch(error => {
        error_popup('Error adding Section:', error)
    });
}

function get_all_Sections() {
    let semester    = document.getElementById('Section_Semester').value;
    let course      = document.getElementById('Section_Course_ID').value;
    let schedule    = document.getElementById('Section_Schedule').value;
    let instructor  = document.getElementById('Section_Instructor').value;

    semester    = semester.trim()   === "" ? "NULL":semester     
    course      = course.trim()     === "" ? "NULL":course       
    schedule    = schedule.trim()   === "" ? "NULL":schedule     
    instructor  = instructor.trim() === "" ? "NULL":instructor   

    const queryParams = new URLSearchParams({
        Section_ID: "NULL",
        Section_Semester: semester,
        Section_Course_ID: course,
        Section_Schedule: schedule,
        Section_Instructor: instructor
    }).toString();

    fetch(`/api/get/Sections?${queryParams}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            if (data.filename) {
                download_file(data.filename)
                alert("Success!")
            }
            else {
                const semester    = document.getElementById('Section_Semester');
                const course      = document.getElementById('Section_Course_ID');
                const schedule    = document.getElementById('Section_Schedule');
                const instructor  = document.getElementById('Section_Instructor');
    
                semester.value = data.Section_Semester;
                course.value = data.Section_Course_ID;
                schedule.value = data.Section_Schedule;
                instructor.value = data.Section_Instructor;
    
                alert("Success! ID Was: " + data.Section_ID)
            }
        }
        else {
            error_popup('Error searching for Section:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Section:', error)
    });
}




function search_student() {
    const id = document.getElementById('Student_ID').value;

    fetch(`/api/get/Students?Student_ID=${id}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            const name      = document.getElementById('Student_Name');
            const address   = document.getElementById('Student_Address');
            const email     = document.getElementById('Student_Email');

            name.value = data.Student_Name;
            address.value = data.Student_Address;
            email.value = data.Student_Email;

            alert("Success! ID Was: " + data.Student_ID)
        }
        else {
            error_popup('Error searching for Student:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Student:', error)
    });
}

function delete_student() {

}

function modify_student() {

}

function add_student() {
    const name      = document.getElementById('Student_Name').value;
    const address   = document.getElementById('Student_Address').value;
    const email    = document.getElementById('Student_Email').value;

    const data = {
        Student_Name: name,
        Student_Address: address,
        Student_Email: email
    };

    fetch('/api/post/Students', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        console.log('ID Was: ', data.Student_ID);
        alert("Success! ID Was: " + data.Student_ID)
    })
    .catch(error => {
        error_popup('Error adding Student:', error)
    });
}

function get_all_Students() {
    let name      = document.getElementById('Student_Name').value;
    let address   = document.getElementById('Student_Address').value;
    let email     = document.getElementById('Student_Email').value;
    
    name    = name.trim()       === "" ? "NULL":name     
    address = address.trim()    === "" ? "NULL":address  
    email   = email.trim()      === "" ? "NULL":email    

    const queryParams = new URLSearchParams({
        Student_ID: "NULL",
        Student_Name: name,
        Student_Address: address,
        Student_Email: email
    }).toString();

    fetch(`/api/get/Students?${queryParams}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            if (data.filename) {
                download_file(data.filename)
                alert("Success!")
            }
            else {
                const name      = document.getElementById('Student_Name');
                const address   = document.getElementById('Student_Address');
                const email     = document.getElementById('Student_Email');
            
                name.value = data.Student_Name;
                address.value = data.Student_Address;
                email.value = data.Student_Email;
            
                alert("Success! ID Was: " + data.Student_ID)
            }
        }
        else {
            error_popup('Error searching for Student:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Student:', error)
    });
}




function search_registration() {
    const id = document.getElementById('Registration_ID').value;

    fetch(`/api/get/Registrations?Registration_ID=${id}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            const section   = document.getElementById('Registration_Section_ID');
            const student   = document.getElementById('Registration_Student_ID');
            const grade     = document.getElementById('Registration_Grade');

            section.value = data.Registration_Section_ID;
            student.value = data.Registration_Student_ID;
            grade.value = data.Registration_Grade;

            alert("Success! ID Was: " + data.Registration_ID)
        }
        else {
            error_popup('Error searching for Registration:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Registration:', error)
    });
}

function delete_registration() {

}

function modify_registration() {

}

function add_registration() {
    const section   = document.getElementById('Registration_Section_ID').value;
    const student   = document.getElementById('Registration_Student_ID').value;
    const grade     = document.getElementById('Registration_Grade').value;

    const data = {
        Registration_Section_ID: section,
        Registration_Student_ID: student,
        Registration_Grade: grade
    };

    fetch('/api/post/Registrations', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        console.log('ID Was: ', data.Registration_ID);
        alert("Success! ID Was: " + data.Registration_ID)
    })
    .catch(error => {
        error_popup('Error adding Registration:', error)
    });
}

function get_all_Registrations() {
    let section   = document.getElementById('Registration_Section_ID');
    let student   = document.getElementById('Registration_Student_ID');
    let grade     = document.getElementById('Registration_Grade');
    
    section = section.trim()    === "" ? "NULL":section  
    student = student.trim()    === "" ? "NULL":student  
    grade   = grade.trim()      === "" ? "NULL":grade    

    const queryParams = new URLSearchParams({
        Registration_ID: "NULL",
        Registration_Section_ID: section,
        Registration_Student_ID: student,
        Registration_Grade: grade
    }).toString();

    fetch(`/api/get/Registrations?${queryParams}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.status);
        if (data.status == "success") {
            if (data.filename) {
                download_file(data.filename)
                alert("Success!")
            }
            else {
                const section   = document.getElementById('Registration_Section_ID');
                const student   = document.getElementById('Registration_Student_ID');
                const grade     = document.getElementById('Registration_Grade');
    
                section.value = data.Registration_Section_ID;
                student.value = data.Registration_Student_ID;
                grade.value = data.Registration_Grade;
    
                alert("Success! ID Was: " + data.Registration_ID)
            }
        }
        else {
            error_popup('Error searching for Registration:', 0)
        }
    })
    .catch(error => {
        error_popup('Error searching for Registration:', error)
    });
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