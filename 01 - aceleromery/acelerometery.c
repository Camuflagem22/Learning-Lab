/* Welcome to Acelerometry, made by Sky23walker. Please make sure that:
    - The data file is named 'inputdata.txt'
    - the components are in order x, y, z
    - the value is either alone or starts with a letter, like x, y, z
       example: 0.75  or  x0.75
    - The first line of the Data File is the first line with data;
    - Each line has a maximum of 250 characters;
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Function Prototypes */
void writeUntil( char *arrivalVector, const char *originVector, int startIndex, 
                 char terminator );
int proxima( const char *vector, int startIndex, char key );
int startAt( int column, const char *buffer, int startIndex, char key);


int main( void ){
    /*  Startup Section  */
    FILE *pFile = fopen("inputdata.txt", "r");
    char buffer[256];   /* Stores a copy of an entire line. */
    char answer[10];    /* Stores input from the user. */
    int lines;          /* Number of lines to be considered. */
    int column;         /* Column where the acelerometer data starts. */
    int startIndex = 0;
    char key;
    int i;

    char holder[10];
    double acX;
    double acY;
    double acZ;

    /* Checks if the file can be opened or not. */
    if(pFile == NULL){
        printf("Error: 'inputdata.txt' not found on this folder.\n\n");
        printf("Program finished. enter any key to exit: ");
        fgets(buffer, 256, stdin);
        return -1;
    } else{ 
        printf("Inicializing Data File.\n\n");
    }

    /* DEBUG ONLY LINES */
    //fgets(buffer, 256, pFile);
    //printf("First line of your file: \n%s\n", buffer);

    /*  Inicial Inputs Section  */
    printf("Enter how many LINES to consider: ");
    fgets(answer, 8, stdin);
    while(atoi(answer) == 0){
        printf("Error: The number must be a positive integer.\n How many LINES: ");
        fgets(answer, 8, stdin);
    }
    lines = atoi(answer);

    printf("\nStarting position is the first COLUMN where the acelerometer data starts.");
    printf("\nEnter the starting position of your data: ");
    fgets(answer, 8, stdin);
    while(atoi(answer) == 0){
        printf("Error: The number must be a positive integer.\n Starting COLUMN: ");
        fgets(answer, 8, stdin);
    }
    column = atoi(answer);

    printf("\nSpearation key is set to ';' (edit variable key at line 70)\n\n");
    key = ';';

    /* Getting the Acelerometer Data */
    double vec_acX[lines];
    double vec_acY[lines];
    double vec_acZ[lines];

    for(i = 1; i <= lines; i++){
        fgets(buffer, 256, pFile);          /* to read a line */
        startIndex = startAt(column, buffer, startIndex, key);
        //printf("%d\n", startIndex);         /* for debug only */

        /*  Getting the x component  */
        if( isdigit(buffer[startIndex]) == 0 && buffer[startIndex] != '-' &&
             buffer[startIndex] != '0' ){
            writeUntil(holder, buffer, startIndex + 1, key);
            acX = atof(holder);
            //printf("%lf", acX);           /* for debug only */
            }
        else{
            writeUntil(holder, buffer, startIndex, key);
            acX = atof(holder);
            //printf("%lf", acX);           /* for debug only */
            }
        vec_acX[ i-1 ] = acX;

        startIndex = (proxima(buffer, startIndex, key)) + 1;
        //printf("%d\n", startIndex);         /* for debug only */

        /*  Getting the y component  */
        if( isdigit(buffer[startIndex]) == 0 && buffer[startIndex] != '-' &&
             buffer[startIndex] != '0' ){
            writeUntil(holder, buffer, startIndex + 1, key);
            acY = atof(holder);
            //printf("    %lf", acY);           /* for debug only */
            }
        else{
            writeUntil(holder, buffer, startIndex, key);
            acY = atof(holder);
            //printf("    %lf", acY);           /* for debug only */
            }
        vec_acY[ i-1 ] = acY;

        startIndex = (proxima(buffer, startIndex, key)) + 1;
        //printf("%d\n", startIndex);         /* for debug only */

        /*  Getting the z component  */
        if( isdigit(buffer[startIndex]) == 0 && buffer[startIndex] != '-' &&
             buffer[startIndex] != '0' ){
            writeUntil(holder, buffer, startIndex + 1, key);
            acZ = atof(holder);
            //printf("    %lf\n", acZ);           /* for debug only */
            }
        else{
            writeUntil(holder, buffer, startIndex, key);
            acZ = atof(holder);
            //printf("    %lf\n", acZ);           /* for debug only */
            }
        vec_acZ[ i-1 ] = acZ;

        startIndex = 0;         /* to reset startIndex */
    }
    /*By now the acelerometer data should be stored inside 3 arrays. That is the data 
       the programs will be able to use.*/

    /*  Calculating the norm of the aceleration vector  */
    double vec_norms[lines];
    printf("\nList of vector norms (in g):\n");
    for(i = 0; i < lines; i++){
        vec_norms[i] = sqrt( pow(vec_acX[i], 2) + pow(vec_acY[i], 2) + pow(vec_acZ[i], 2));
        printf("%lf\n", vec_norms[i]);
    }
    fclose(pFile);

    printf("\nDo you wish to save the results a file (outputdata.txt)? [Y/n]: ");
    fgets(answer, 8, stdin);
    while(answer[0] != 'Y' && answer[0] != 'n'){
        printf("Invalid answer. [Y/n]: ");
        fgets(answer, 8, stdin);
    }
    if(answer[0] == 'Y'){
        FILE *pFile = fopen("outputdata.txt", "w");
        for(i = 0; i < lines; i++){
            fprintf(pFile, "%lf\n", vec_norms[i]);
        }
        fclose(pFile);
    }


    /*  Finish Section  */
    printf("Program finished. Enter any key to exit: ");
    fgets(buffer, 256, stdin);
    return 0;
}



/*
> This funtion copies the originVector to the arrivalVector, starting on the
    startIndex, until it reaches the terminator character.
*/
void writeUntil( char *arrivalVector, const char *originVector, int startIndex, 
                 char terminator ){
    int i = 0;                /* counter for arrivalVector */
    int j = startIndex;       /* counter for originVector */

    while ( originVector[j] != terminator ){
        arrivalVector[i] = originVector[j];
        i++;
        j++;
    }
    arrivalVector[i] = '\0';
}

/*
> Given a startIndex, this function searches vector for the next character that is 
    equal to the key character. If it is not found, the function returns -1.
*/
int proxima( const char *vector, int startIndex, char key ){
    int j = startIndex;       /* counter for vector */

    while ( vector[j] != key  && vector[j] != '\0' ){
        j++;
    }
    if ( vector[j]  == '\0' ){
        j = -1;
    }
    return j;
}

/*
> Given a targen column, this function determines the correct startIndex for the buffer.
*/
int startAt( int column, const char *buffer, int startIndex, char key){
    int i;
    for(i = 0; i < (column -1); i++){
        startIndex = proxima(buffer, startIndex, key) + 1;
    }
    return startIndex;
}