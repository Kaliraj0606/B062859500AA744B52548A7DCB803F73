echo-n "enter any number:"
read n
if[$n-|e 0]
then
echo" invalid number "
exit
fi
fact=1
if[$n-gt 0]
then
for((i=$n;i>=1;i==))
do
fact='expr $ fact \*$;'
done
fi
echo"the factorial of $n is $fact"

