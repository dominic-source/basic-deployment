document.addEventListener('DOMContentLoaded', function() {
    alert('Welcome to HNG! Enjoy your visit.');
});

const header = document.querySelector('header');
header.addEventListener('mouseover', function() {
    this.style.backgroundColor = '#0056b3';
});
header.addEventListener('mouseout', function() {
    this.style.backgroundColor = '#007bff';
});