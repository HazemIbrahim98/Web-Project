<?php
$var = $_POST["var"];

session_start();

if (isset($_SESSION[$var])) {
    echo $_SESSION[$var];
}
