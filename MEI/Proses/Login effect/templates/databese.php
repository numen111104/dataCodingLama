<?php
$servername = "waffenbruder.site";
$username = "numannasyarmz11@gmail.com";
$password = "tidore191104";
$dbname = "sqlite:///example_database.db";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>
