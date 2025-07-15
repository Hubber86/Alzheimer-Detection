document.addEventListener('DOMContentLoaded', function () {
    // Improved Notifications
    function showNotification(message, type) {
        const notificationDiv = document.createElement('div');
        notificationDiv.className = `alert alert-${type} mt-2`;
        // Set the color based on the type of message
        if (type === 'success') {
            notificationDiv.classList.add('alert-success');
        } else if (type === 'error' || type === 'danger') {
            notificationDiv.classList.add('alert-danger');
        } else {
            // Default to danger color if the type is not recognized
            notificationDiv.classList.add('alert-danger');
        }

        notificationDiv.textContent = message;
        // Add the notification to the top of the page
        document.body.insertBefore(notificationDiv, document.body.firstChild);

        // Automatically remove the notification after a few seconds
        setTimeout(() => {
            notificationDiv.remove();
        }, 5000);
    }

    // Part 1: Upload Form
    const uploadForm = document.getElementById('uploadForm');

    if (uploadForm) {
        uploadForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const fileInput = document.getElementById('fileInput');
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirm_password');

            // Validate the form fields
            if (!fileInput || fileInput.files.length === 0 || !password || !confirmPassword) {
                showNotification('Please fill in all required fields.', 'danger');
                return;
            }

            const file = fileInput.files[0];

            // Additional client-side validation (you can customize this)
            if (password.value !== confirmPassword.value) {
                showNotification('Passwords do not match. Please try again.', 'danger');
                return;
            }

            const formData = new FormData();
            formData.append('file', file);

            fetch('/predict', {
                method: 'POST',
                body: formData,
            })
                .then(response => {
                    if (response.ok) {
                        showNotification('File uploaded successfully!', 'success');
                        window.location.href = '/performance';
                    } else {
                        return response.json();
                    }
                })
                .then(data => {
                    if (data) {
                        showNotification(data.error || 'Something went wrong.', 'danger');
                        console.log(data);
                    }
                })
                .catch(error => {
                    showNotification('Error uploading file.', 'danger');
                    console.error('Error:', error);
                })
                .finally(() => {
                    // Reset the file input after a successful upload
                    fileInput.value = null;
                });
        });
    } else {
        showNotification('Upload form not found.', 'danger');
        console.error("Upload form element not found.");
    }

    // Part 3: Password Matching
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const passwordMismatch = document.getElementById("passwordMismatch");
    const passwordError = document.getElementById("password_error");

    if (password && confirmPassword && passwordMismatch && passwordError) {
        function checkPassword() {
            if (password.value !== confirmPassword.value) {
                passwordMismatch.style.display = "block";
            } else {
                passwordMismatch.style.display = "none";
                // Reset the error message
                passwordError.innerHTML = "";
            }
        }

        password.addEventListener("input", checkPassword);
        confirmPassword.addEventListener("input", checkPassword);

        // Part 4: Password Validation
        function validatePassword() {
            const passwordValue = password.value;
            const confirmPasswordValue = confirmPassword.value;

            if (!passwordValue.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/)) {
                passwordError.innerHTML = "Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.";
                return false;
            }

            if (passwordValue !== confirmPasswordValue) {
                passwordError.innerHTML = "Passwords do not match.";
                return false;
            }

            // Reset the error message
            passwordError.innerHTML = "";

            return true;
        }

        // Add validation function to the form submission
        uploadForm.addEventListener('submit', function (event) {
            if (!validatePassword()) {
                // Prevent form submission if validation fails
                event.preventDefault();
            }
        });
    } else {
        console.error("One or more password-related elements not found.");
    }

    // Your JavaScript code goes here
    // Add any client-side logic or interactivity

    // Example: Activate tabs functionality
    const tabs = document.querySelectorAll('.tabs a');
    tabs.forEach(tab => {
        tab.addEventListener('click', function (e) {
            e.preventDefault();
            const tabId = this.getAttribute('href').substring(1);
            showTab(tabId);
        });
    });

    function showTab(tabId) {
        const tabContents = document.querySelectorAll('.tab-content');
        tabContents.forEach(content => {
            content.style.display = 'none';
        });

        const selectedTab = document.getElementById(tabId);
        if (selectedTab) {
            selectedTab.style.display = 'block';
        }
    }

    // Example: File upload related interactions
    const fileInput = document.getElementById('fileInput');
    if (fileInput) {
        fileInput.addEventListener('change', function () {
            const fileNameDisplay = document.getElementById('fileNameDisplay');
            if (fileNameDisplay) {
                fileNameDisplay.textContent = this.files[0].name;
            }
        });
    }
});
