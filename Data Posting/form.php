<?php
function abc(){
    echo('abc');
    echo(isset($_POST['btn']));

    if(isset($_POST['btn'])){
        echo('hello');
    }
}
?>