<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "database";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn)
    echo "<script>console.log('Connected successfully');</script>";
else
    echo "<script>console.log('Error Connectign to Database');</script>";
