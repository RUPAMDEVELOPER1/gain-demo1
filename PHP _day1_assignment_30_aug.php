//1


<?php
function calculateDebt($n) {
    $borrowingAmount = 100000;
    $interestRate = 0.05;

    $debt = $borrowingAmount;
    
    for ($i = 0; $i < $n; $i++) {
        $interest = $debt * $interestRate;
        $debt += $interest;
        
        // Round debt to the nearest 1000
        $debt = ceil($debt / 1000) * 1000;
    }
    
    return $debt;
}

// Input: Number of months (n)
$n = 12; // You can change this to any value between 0 and 100

$finalDebt = calculateDebt($n);

echo "Amount of debt after $n months: $finalDebt";
?>
Replace the value of $n with the desired number of months (between 0 and 100) to calculate the corresponding debt amount after that period. The program calculates the debt by applying the interest rate each month and rounding it up to the nearest thousand.




//2<?php
function areSegmentsOrthogonal($xp, $yp, $xq, $yq, $xr, $yr, $xs, $ys) {
    // Direction vectors of segments AB and CD
    $vectorAB = [$xq - $xp, $yq - $yp];
    $vectorCD = [$xs - $xr, $ys - $yr];
    
    // Calculate the dot product of the direction vectors
    $dotProduct = $vectorAB[0] * $vectorCD[0] + $vectorAB[1] * $vectorCD[1];
    
    // Check if the dot product is approximately equal to 0
    // Use a small threshold due to potential floating-point precision issues
    $threshold = 1e-10;
    if (abs($dotProduct) < $threshold) {
        return true; // Segments are orthogonal
    } else {
        return false; // Segments are not orthogonal
    }
}

// Sample input coordinates
$xp = 0.0;
$yp = 0.0;
$xq = 0.0;
$yq = 5.0;
$xr = 0.0;
$yr = 0.0;
$xs = 3.0;
$ys = 0.0;

// Check if the segments are orthogonal
if (areSegmentsOrthogonal($xp, $yp, $xq, $yq, $xr, $yr, $xs, $ys)) {
    echo "Segments AB and CD are orthogonal.";
} else {
    echo "Segments AB and CD are not orthogonal.";
}
?>


//3
<?php
function circleRelationship($x1, $y1, $r1, $x2, $y2, $r2) {
    $distanceBetweenCenters = sqrt(($x2 - $x1)**2 + ($y2 - $y1)**2);
    
    if ($distanceBetweenCenters + $r2 <= $r1) {
        return "C2 is in C1.";
    } elseif ($distanceBetweenCenters + $r1 <= $r2) {
        return "C1 is in C2.";
    } elseif ($distanceBetweenCenters < $r1 + $r2) {
        return "Circumference of C1 and C2 intersect.";
    } else {
        return "C1 and C2 do not overlap.";
    }
}

// Sample input coordinates and radii
list($r1, $x1, $y1, $r2, $x2, $y2) = explode(" ", readline());
echo circleRelationship($x1, $y1, $r1, $x2, $y2, $r2);
?>
