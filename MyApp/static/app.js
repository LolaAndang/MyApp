
document.addEventListener("DOMContentLoaded", function () {
    const html = document.documentElement;
    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");

    // Restore the previously selected theme.
    let savedTheme = "light";

    try {
        savedTheme = localStorage.getItem("studyflow-theme") || "light";
    } catch (error) {
        // Continue with the light theme if storage is unavailable.
    }

    function applyTheme(theme) {
        const isDark = theme === "dark";

        html.setAttribute("data-theme", isDark ? "dark" : "light");

        if (themeIcon) {
            themeIcon.setAttribute(
                "data-lucide",
                isDark ? "sun" : "moon"
            );
        }

        if (themeToggle) {
            themeToggle.setAttribute(
                "aria-label",
                isDark ? "Switch to light mode" : "Switch to dark mode"
            );

            themeToggle.setAttribute(
                "title",
                isDark ? "Switch to light mode" : "Switch to dark mode"
            );
        }

        const themeColor = document.querySelector(
            'meta[name="theme-color"]'
        );

        if (themeColor) {
            themeColor.setAttribute(
                "content",
                isDark ? "#191722" : "#f7f6fb"
            );
        }

        // Re-render the Lucide icon after changing its name.
        if (window.lucide) {
            window.lucide.createIcons();
        }
    }

    applyTheme(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const currentTheme = html.getAttribute("data-theme");
            const nextTheme = currentTheme === "dark" ? "light" : "dark";

            applyTheme(nextTheme);

            try {
                localStorage.setItem("studyflow-theme", nextTheme);
            } catch (error) {
                // Theme still changes for the current page.
            }
        });
    }

    // Animate the dashboard progress bar.
    const progressFill = document.querySelector(".progress-fill");

    if (progressFill) {
        const targetWidth = progressFill.dataset.progress || "0%";

        progressFill.style.width = "0%";

        requestAnimationFrame(function () {
            progressFill.style.width = targetWidth;
        });
    }

    // Initialize icons for any elements rendered by Django.
    if (window.lucide) {
        window.lucide.createIcons();
    }
});
