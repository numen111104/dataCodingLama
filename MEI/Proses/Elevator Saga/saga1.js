{
    init: function(elevators, floors) {
        var elevator = elevators[0]; // Let's use the first elevator
        var elevator1 = elevators[1];
        var elevnumen = elevators[2];
        var elevzul = elevators[3];

        // Whenever the elevator is idle (has no more queued destinations) ...
        elevator.on("idle", function() {
            // let's go to all the floors (or did we forget one?)
            elevator.goToFloor(0);
            elevator.goToFloor(5);
            elevator.goToFloor(4);
            elevator.goToFloor(3);
            elevator.goToFloor(0);
            elevator.goToFloor(1);
            elevator.goToFloor(2);
            elevator.goToFloor(3);
            elevator.goToFloor(4);
        });
         elevator1.on("idle", function() {
            elevator1.goToFloor(0);
            elevator1.goToFloor(2);
            elevator1.goToFloor(3);
            elevator1.goToFloor(0);
            elevator1.goToFloor(4);
            elevator1.goToFloor(5);
            elevator1.goToFloor(3);
            elevator1.goToFloor(1);
        });
        elevnumen.on("idle", function() {
            elevnumen.goToFloor(0);
            elevnumen.goToFloor(1);
            elevnumen.goToFloor(2);
            elevnumen.goToFloor(3);
            elevnumen.goToFloor(0);
            elevnumen.goToFloor(4);
            elevnumen.goToFloor(5);
        });
        elevzul.on("idle", function() {
            elevzul.goToFloor(0);
            elevzul.goToFloor(3);
            elevzul.goToFloor(5);
            elevzul.goToFloor(0);
            elevzul.goToFloor(4);
            elevzul.goToFloor(2);
            elevzul.goToFloor(1);
        });
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}