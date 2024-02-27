<?php
include('server.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Posting</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Students Form</h1>
        <form action="#" method="GET">
            <label><span>Employee No.</span> <input type="number" name="empno" id="empno" required></label>
            <label><span>Employee Name</span> <input type="text" name="ename" id="ename" required></label>
            <label><span>Employee Salary</span> <input type="number" name="esal" id="esal" required></label>
            
            <input type="submit" value="Submit" id='btn' name='btn'>
        </form>

        <?php
         $name = '';
         $no = '';
         $sal= '';
        if (isset($_GET['btn'])) {
           $name = $_GET['ename'];
           $no = $_GET['empno'];
           $sal= $_GET['esal'];

           $query = "insert into emp values ('$no','$name', '$sal')";
           $empq = mysqli_query($connection, $query);

           if($empq){
            echo('data inserted');
           }
        }
        ?>

        <table border>
            <thead>
                <tr>
                    <th>Employee No.</th>
                    <th>Employee Name</th>
                    <th>Employee Salary</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><?php echo($no); ?></td>
                    <td><?php echo($name); ?></td>
                    <td><?php echo($sal); ?></td>
                </tr>
            </tbody>
        </table>

    </div>
</body>
</html>