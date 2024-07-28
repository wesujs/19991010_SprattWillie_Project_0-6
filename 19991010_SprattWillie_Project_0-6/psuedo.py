START

DEFINE FILENAME as 'allowed_vehicles.txt'

FUNCTION read_vehicles_from_file
    IF file FILENAME exists THEN
        OPEN FILENAME for reading
        READ all lines from FILENAME into list vehicles
        CLOSE file
    ELSE
        INITIALIZE vehicles with default list of authorized vehicles
        CALL write_vehicles_to_file with vehicles
    ENDIF
    RETURN vehicles
END FUNCTION

FUNCTION write_vehicles_to_file(vehicles)
    OPEN FILENAME for writing
    FOR each vehicle in vehicles DO
        WRITE vehicle to FILENAME
    ENDFOR
    CLOSE file
END FUNCTION

FUNCTION print_authorized_vehicles(vehicles)
    PRINT "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
    FOR each make in vehicles DO
        PRINT make
    ENDFOR
END FUNCTION

FUNCTION search_authorized_vehicle(vehicles)
    PROMPT user for vehicle name input into search
    IF search in vehicles THEN
        PRINT search is an authorized vehicle
    ELSE
        PRINT search is not an authorized vehicle, check spelling and try again
    ENDIF
END FUNCTION

FUNCTION add_authorized_vehicle(vehicles)
    PROMPT user for new vehicle input into new_add
    ADD new_add to vehicles
    CALL write_vehicles_to_file with vehicles
    PRINT new_add has been added as an authorized vehicle
END FUNCTION

FUNCTION delete_authorized_vehicle(vehicles)
    PROMPT user for vehicle name to remove input into new_delete
    PROMPT user for confirmation input into assurance
    IF assurance equals "yes" THEN
        IF new_delete in vehicles THEN
            REMOVE new_delete from vehicles
            CALL write_vehicles_to_file with vehicles
            PRINT new_delete has been removed as an authorized vehicle
        ELSE
            PRINT Vehicle new_delete not found in the list
        ENDIF
    ELSE
        PRINT Operation cancelled
    ENDIF
END FUNCTION

FUNCTION onLoad
    CALL read_vehicles_from_file
    STORE result in AllowedVehiclesList

    DISPLAY menu and get user input into execution

    IF execution equals 1 THEN
        CALL print_authorized_vehicles with AllowedVehiclesList
        CALL onLoad

    ELSE IF execution equals 2 THEN
        CALL search_authorized_vehicle with AllowedVehiclesList
        CALL onLoad

    ELSE IF execution equals 3 THEN
        CALL add_authorized_vehicle with AllowedVehiclesList
        CALL onLoad

    ELSE IF execution equals 4 THEN
        CALL delete_authorized_vehicle with AllowedVehiclesList
        CALL onLoad

    ELSE IF execution equals 5 THEN
        PRINT goodbye message

    ELSE
        PRINT invalid option message
        CALL onLoad
    ENDIF
END FUNCTION

CALL onLoad

END
