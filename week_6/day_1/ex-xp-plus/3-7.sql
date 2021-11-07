select first_name, last_name from students where substring(reverse(first_name),2,1) = 'a';
