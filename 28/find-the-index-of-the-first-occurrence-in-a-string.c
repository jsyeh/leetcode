int strStr(char * haystack, char * needle){
    char* pos = strstr(haystack, needle);
    if(pos==NULL) return -1;
    else return pos - haystack;
}
