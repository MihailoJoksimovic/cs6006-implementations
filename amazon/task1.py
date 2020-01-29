# So here is the idea:
#   1. We will need a hashmap to keep track of number of feature requests, obviously
#   2. We will need to iterate through words. Now, one possible option is to just split
#       by space. That's an easier option but it will take additional space obviously.
#       The better option for sure is to use some more efficient algoritghm (Rapin-karp?),
#       OR maybe we can do it with two pointers. This would do it in O(n) time WITHOUT
#       additional space complexity. And that's good!
#   3. Finally, we need to have a list of TOP features. I yet have to see how
#       to go from hashmap to top-n stuff.


# Debt:
#   1. High space complexity in getFeatureCountsInFeatureRequest(). Would be better to replace with something linear?


def getFeatureCountsInFeatureRequest(featureRequest, possibleFeatures):
    frequencies = {}

    # NOTE: HIGH-SPACE COMPLEXITY!!
    for word in featureRequest.split(" "):
        if word.lower() in possibleFeatures and word not in frequencies:
            frequencies[word.lower()] = 1

    return frequencies



def popularNFeatures(numFeatures, topFeatures, possibleFeatures,
                    numFeatureRequests, featureRequests):


        frequencies = {feature.lower(): 0 for feature in possibleFeatures}

        for featureRequest in featureRequests:
            occurences = {}

            featureRequestLen = len(featureRequest)

            for feature in possibleFeatures:
                featureLen = len(feature)

                i = 0

                while True:
                    if featureRequest[i:featureLen].lower() == feature and feature not in occurences:
                        occurences[feature] = True

                        frequencies[feature] += 1

                    i += featureLen

                    if i > (featureRequestLen - featureLen):
                        break

        sorted_feature_counts = [k for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)]



        return sorted(sorted_feature_counts[0:topFeatures])

        # technically, we could actually use array as well instead of a hashmap?
        overall_feature_counts = {}

        for featureRequest in featureRequests:
            feature_counts = getFeatureCountsInFeatureRequest(featureRequest, possibleFeatures)

            for feature in feature_counts:
                if feature not in overall_feature_counts:
                    overall_feature_counts[feature] = 1

                    continue

                overall_feature_counts[feature] += 1

        # Convert hashmap to array now, sort it and return top features

        sorted_feature_counts = {k: v for k, v in sorted(overall_feature_counts.items(), key=lambda item: item[1], reverse=True)}

        i = 0

        out = {}

        for k, v in sorted_feature_counts.items():
            out[k] = v

            i += 1

            if i >= topFeatures:
                break

        return sorted([v for v in out])


out = popularNFeatures(3, 1, ['anacell', 'betacellular', 'cetracular'], 5,

                     ['Anacell is very nice but betacellular rocks', 'I love anacell Best services provided by anacell in the town', 'betacellular has great services', 'deltacellular provides much better services than betacellular', 'cetracular is worse than eurocell', 'betacellular is better than deltacellular'],
)

print(out)

