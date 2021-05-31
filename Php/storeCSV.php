<?php
if (!empty($_POST['data'])) {
    $data = $_POST['data'];

    $file = fopen("../PythonBackend/" . "DATASET.csv", 'w');
    fwrite($file, $data);
    fclose($file);
}
