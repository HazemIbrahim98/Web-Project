<?php
require_once "connect.php";

$email = $_POST["email"];

$sql = "DELETE FROM `users` WHERE email = '" . $email . "'";

$result = mysqli_query($conn, $sql);

mysqli_close($conn);
