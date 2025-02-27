class Solution:
  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    answer = []
    
    # interval -> [0, 1]

    for interval in sorted(intervals):
      if not answer or answer[-1][1] < interval[0]: # answer[-1][1] : index 1 of latest element in answer
        answer.append(interval)
      else:
        answer[-1][1] = max(answer[-1][1], interval[1]) # interval[1] : index 1 of current interval

    return answer