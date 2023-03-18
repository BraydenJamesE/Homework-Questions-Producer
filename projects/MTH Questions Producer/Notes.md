# Notes File

## To Do

- Need a new function or check of some kind that ensures values in the review section are not also being output in the non-review section. I only want unique values, and with the current model, if I select 0, I get unique values in each list. But, when looking at these lists in totality, there is a lot of the same values.
- Need a new function that adds the unit to the items in the list
- Need a new function that sorts the list (my intuition says that this will need to be sorted before adding the unit)
- Need a new statement that allows for more effenciency. If I ask for a large amount of items, the program runs for awhile because it is selecting random indexs and doesn't want to use already existing ones. Thus, what we get is a lot of wait time as it looks for unique values. The best method may be to presort the list, and then pick values in order or a already randomized list.

## Considerations

Consider adding a function that allows the user to assess the number of days to study compared with the number of problems available and gives a value that the user would be required to do per day.
