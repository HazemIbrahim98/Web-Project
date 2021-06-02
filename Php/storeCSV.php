<?php
if (!empty($_POST['data'])) {
    $data = $_POST['data'];


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
