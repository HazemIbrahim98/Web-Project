<?php
if (!empty($_POST['data'])) {
    $data = $_POST['data'];

    ini_set("session.gc_maxlifetime", 5);
    ini_set("session.cookie_lifetime", 5);
    session_start();

    try {
        $path = "../Dataset/" . $_SESSION["name"] . "/dataset.csv";
        $file = fopen($path, 'w');
        fwrite($file, $data);
        fclose($file);
    } catch (Exception $e) {
        echo $e;
    }
}
