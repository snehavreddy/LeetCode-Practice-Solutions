class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        minLandFinish = min(
            s + d for s, d in zip(landStartTime, landDuration)
        )

        ans1 = float('inf')
        for s, d in zip(waterStartTime, waterDuration):
            ans1 = min(ans1, max(minLandFinish, s) + d)

        minWaterFinish = min(
            s + d for s, d in zip(waterStartTime, waterDuration)
        )

        ans2 = float('inf')
        for s, d in zip(landStartTime, landDuration):
            ans2 = min(ans2, max(minWaterFinish, s) + d)

        return min(ans1, ans2)