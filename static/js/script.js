// General script for interactivity

document.addEventListener("DOMContentLoaded", () => {
    console.log("Page loaded successfully");

    // Dropdown functionality
    const dropdowns = document.querySelectorAll(".dropdown-toggle");
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("click", (e) => {
            const menu = e.target.nextElementSibling;
            if (menu) {
                menu.classList.toggle("show");
            }
        });
    });

    // Close dropdowns when clicking outside
    window.addEventListener("click", (e) => {
        if (!e.target.matches(".dropdown-toggle")) {
            document.querySelectorAll(".dropdown-menu.show").forEach(menu => {
                menu.classList.remove("show");
            });
        }
    });

    // Form submission handling
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            console.log("Form submitted:", new FormData(form));
            alert("Form submitted successfully!");
        });
    });

    // Table row hover effect (optional)
    const tableRows = document.querySelectorAll("table tbody tr");
    tableRows.forEach(row => {
        row.addEventListener("mouseenter", () => row.style.backgroundColor = "#f1f1f1");
        row.addEventListener("mouseleave", () => row.style.backgroundColor = "");
    });

    // Add new row to table
    const addRowButton = document.getElementById("add-row");
    if (addRowButton) {
        addRowButton.addEventListener("click", () => {
            const tableBody = document.querySelector("table tbody");
            const newRow = document.createElement("tr");
            newRow.innerHTML = `
                <td>New ID</td>
                <td>New Name</td>
                <td>New Email</td>
                <td>New Phone</td>
                <td>$0.00</td>
                <td><a href="#">View</a></td>
                <td><span class="badge badge-soft-success">New Status</span></td>
                <td>New Date</td>
                <td>New Sent</td>
                <td><i class="fas fa-ellipsis-v"></i></td>
            `;
            tableBody.appendChild(newRow);
        });
    }

    // Open PDF preview modal
    const pdfPreviewButtons = document.querySelectorAll(".btn-preview");
    pdfPreviewButtons.forEach(button => {
        button.addEventListener("click", () => {
            const modal = document.getElementById("pdf-preview-modal");
            if (modal) {
                modal.classList.add("show");
                modal.style.display = "block";
            }
        });
    });

    // Close PDF preview modal
    const modalCloseButton = document.getElementById("close-modal");
    if (modalCloseButton) {
        modalCloseButton.addEventListener("click", () => {
            const modal = document.getElementById("pdf-preview-modal");
            if (modal) {
                modal.classList.remove("show");
                modal.style.display = "none";
            }
        });
    };

    // Auto-save settings
    const settingsInputs = document.querySelectorAll(".settings-section input, .settings-section select");
    settingsInputs.forEach(input => {
        input.addEventListener("change", () => {
            console.log(`Auto-saving setting: ${input.id} = ${input.value}`);
            // Simulate an auto-save action (AJAX call can be implemented here)
            setTimeout(() => {
                alert(`Setting '${input.id}' saved successfully!`);
            }, 500);
        });
    });

    // Show loading spinner
    const showSpinner = () => {
        const spinner = document.getElementById("loading-spinner");
        if (spinner) spinner.style.display = "block";
    };

    const hideSpinner = () => {
        const spinner = document.getElementById("loading-spinner");
        if (spinner) spinner.style.display = "none";
    };

    // Simulate a task with spinner
    const simulateTaskButton = document.getElementById("simulate-task");
    if (simulateTaskButton) {
        simulateTaskButton.addEventListener("click", () => {
            showSpinner();
            setTimeout(() => {
                hideSpinner();
                alert("Task completed!");
            }, 2000);
        });
    }

    // Generate PDF functionality
    const generatePdfButton = document.getElementById("generate-pdf");
    if (generatePdfButton) {
        generatePdfButton.addEventListener("click", async () => {
            const data = {
                content: document.getElementById("pdf-content").value,
                header: document.getElementById("pdf-header").value,
                footer: document.getElementById("pdf-footer").value,
                filename: document.getElementById("pdf-filename").value || "document.pdf",
            };

            try {
                const response = await fetch('/generate_pdf', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                const result = await response.json();
                if (result.message) {
                    alert(`PDF generated successfully! You can download it here: ${result.file_path}`);
                } else {
                    alert(`Error: ${result.error}`);
                }
            } catch (error) {
                console.error("Error generating PDF:", error);
                alert("An error occurred while generating the PDF.");
            }
        });
    }
});
