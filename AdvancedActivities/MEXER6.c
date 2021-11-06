#include <stdio.h>
#include <ctype.h>

int main(){

    //attributes
    int hour_enter_time, minute_enter_time, total_hours,total_mins;
    int hour_exit_time, minute_exit_time, round_time;
    int result = 0;
    char vehicle_type;
    int proceed_code = 0;

    printf("What type of vehicle that enters the park?\n");
    printf("C - Car, B - Bus, T - Truck:\t");

    scanf("%c", &vehicle_type);

    switch(toupper(vehicle_type)){
    case 'C':
        printf("\nYou have selected Car\n");
        proceed_code = 1;
        break;
    case 'B':
        printf("\nYou have selected Bus\n");
        proceed_code = 2;
        break;
    case 'T':
        printf("\nYou have selected Truck\n");
        proceed_code = 3;
        break;
    default:
        printf("\nNone of the choices was entered\n");
    }
    if(proceed_code == 0)
        return 0;

    printf("Hour entered:   ");
    scanf("%d",&hour_enter_time);
    printf("Minute entered: ");
    scanf("%d",&minute_enter_time);
    printf("Hour exit:      ");
    scanf("%d",&hour_exit_time);
    printf("Minute exit:    ");
    scanf("%d",&minute_exit_time);


    if(hour_enter_time<hour_exit_time)
        total_hours = hour_exit_time-hour_enter_time;
    else
        total_hours = (24-hour_enter_time)+(hour_exit_time);
    if(minute_enter_time != 0)
        total_mins = (60-minute_enter_time) + (minute_exit_time);
    else
        total_mins = (minute_enter_time) + (minute_exit_time);

    if(total_mins>=60){
        total_hours +=1;
        total_mins -= 60;
    }

    if(total_hours>12)
        round_time = (total_hours - 12) + 1;
    else
        round_time = total_hours+1;

    if(proceed_code == 1){//car
        if(total_hours <= 3){
            result = 0;
        }else{
            result = 5 * (total_hours-3);
        }
    }
    if(proceed_code == 2){//bus
        if(total_hours <= 1){
            result = 2;
        }else{
            result = 2 + 10*((total_hours)-1);
        }
    }
    if(proceed_code == 3){//bus
        if(total_hours <= 2){
            result = 1;
        }else{
            result = 1 + 10*((total_hours)-2);
        }
    }


    printf("========================\n");
    printf("Type of vehicle: ");
    if(proceed_code == 1)
        printf("Car\n");
    else if(proceed_code == 2)
        printf("Bus\n");
    else if(proceed_code == 3)
        printf("Truck\n");
    printf("Time in      : %d:%d\n",hour_enter_time,minute_enter_time);
    printf("Time out     : %d:%d\n",hour_exit_time,minute_exit_time);
    printf("Parking time : %d:%d\n", total_hours,total_mins);
    if(total_hours>12)
        printf("Rounded time : %d:00\n", round_time);
    else
        printf("Rounded time : %d:00\n", round_time);
    printf("_____________________\n");
    printf("Total Charges: %d.00\n", result);

    return 0;
}
