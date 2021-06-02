<?php
$var = $_POST["var"];

ini_set("session.gc_maxlifetime", 0);
ini_set("session.cookie_lifetime", 0);
session_start();

if (isset($_SESSION[$var])) {
    echo $_SESSION[$var];
}
