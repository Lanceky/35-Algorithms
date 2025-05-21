def shipWithinDays(weights, days):
    def can_ship(capacity):
        current_load = 0
        required_days = 1
        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = 0
            current_load += weight
        return required_days <= days

    # Binary search boundaries
    left = max(weights)  # Minimum possible capacity
    right = sum(weights)  # Maximum possible capacity

    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Test
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))  # Output: 15