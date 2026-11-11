#include <vector>
#include <algorithm>

class Solution {
public:
	std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
		std::sort(intervals.begin(), intervals.end(),
			[](const std::vector<int>& a, const std::vector<int>& b)
			{
				return a[0] < b[0];
			});

		std::vector<std::vector<int>> output = {intervals[0]};

		for (int i = 1; i < (int)intervals.size(); i++)
		{
			int start = intervals[i][0];
			int end = intervals[i][1];

			if (start <= output.back()[1])
			{
				output.back()[1] = std::max(output.back()[1], end);
			}
			else
			{
				output.push_back({start, end});
			}
		}
		return output;
	}
};