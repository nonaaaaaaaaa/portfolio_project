// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll(".navbar-nav a");
  
    navLinks.forEach(link => {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = this.getAttribute("href").substring(1);
        const targetElement = document.getElementById(targetId);
  
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop,
            behavior: "smooth"
          });
        }
      });
    });
  
    // Form validation and submission
    const contactForm = document.querySelector("form");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const messageInput = document.getElementById("message");
  
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
  
      // Basic validation
      if (nameInput.value.trim() === "") {
        alert("Please enter your name.");
        nameInput.focus();
        return;
      }
  
      if (emailInput.value.trim() === "") {
        alert("Please enter your email.");
        emailInput.focus();
        return;
      }
  
      if (messageInput.value.trim() === "") {
        alert("Please enter your message.");
        messageInput.focus();
        return;
      }
  
      // Show a thank you message (you could also send the form data to a server here)
      alert("Thank you for contacting us! We will get back to you shortly.");
      contactForm.reset();
    });
  });
  