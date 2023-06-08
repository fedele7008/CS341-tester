#ifndef __TOWER_H__
#define __TOWER_H__

#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>

using std::pair;
using std::swap;
using std::move;
using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::string;

namespace CS341::PQ1 {
    class Tower {
        // Static Field
        static int cid;

        // Private Field
        int id;
        pair<int, int> coordinate;
        int dominance;


    public:
        // Default constructor
        explicit Tower() : id(cid++), coordinate(0, 0), dominance(0) {}

        // Constructor
        explicit Tower(int id, int x, int y) : id(id), coordinate(x, y), dominance(0) {}

        // Constructor
        explicit Tower(int id, int x, int y, int dominance) : id(id), coordinate(x, y), dominance(dominance) {}

        // Destructor
        virtual ~Tower() = default;

        // Copy constructor
        Tower(const Tower &other) = default;

        // Copy operator
        Tower &operator=(const Tower &other) {
            if (this == &other) return *this;
            id = other.id;
            coordinate = other.coordinate;
            dominance = other.dominance;
            return *this;
        }

        // Move constructor
        Tower(Tower &&other) noexcept : id(other.id), coordinate(move(other.coordinate)), dominance(other.dominance) {}

        // Move assignment
        Tower &operator=(Tower &&other) noexcept {
            if (this == &other) return *this;
            id = other.id;
            coordinate = move(other.coordinate);
            dominance = other.dominance;
            return *this;
        }

        // Output stream
        friend std::ostream& operator<<(std::ostream& out, const Tower& tower) {
            out << tower.id << " " << tower.dominance;
            return out;
        }

        // X coordinate getter
        int getX() const noexcept {
            return this->coordinate.first;
        }

        // Y coordinate getter
        int getY() const noexcept {
            return this->coordinate.second;
        }

        // Dominance getter
        int getDominance() const noexcept {
            return this->dominance;
        }

        // ID getter
        int getID() const noexcept {
            return this->id;
        }

        // Dominance setter
        void setDominance(int newDominanceFactor) {
            this->dominance = newDominanceFactor;
        }

        // Increase dominance factor by one
        void increaseDominanceBy(int factor) {
            this->dominance += factor;
        }
    };

    // Initialize static field of Tower
    int Tower::cid = 1;

    namespace helper {
        void findDominanceInUpperRight(Tower *towers, int start, int end) {
            // State terminal condition
            if (start >= end - 1) return;

            // find mid-point index
            int mid = start + (end - start) / 2;

            // divide and conquer
            findDominanceInUpperRight(towers, start, mid);
            findDominanceInUpperRight(towers, mid, end);

            // create left and right temporary copied array
            int leftTowerSize = mid - start;
            int rightTowerSize = end - mid;

            auto *leftTower = new Tower[leftTowerSize];
            auto *rightTower = new Tower[rightTowerSize];

            int leftIndex = 0;
            int rightIndex = 0;
            for (int i = start; i < end; i++) {
                if (i < mid) {
                    leftTower[leftIndex++] = towers[i];
                } else {
                    rightTower[rightIndex++] = towers[i];
                }
            }

            // perform merging and find upper right dominance factor
            leftIndex = 0;
            rightIndex = 0;
            int mergeIndex = start;
            while (leftIndex < leftTowerSize && rightIndex < rightTowerSize) {
                if (leftTower[leftIndex].getY() < rightTower[rightIndex].getY()) {
                    leftTower[leftIndex].increaseDominanceBy(rightTowerSize - rightIndex);
                    towers[mergeIndex++] = leftTower[leftIndex++];
                } else {
                    towers[mergeIndex++] = rightTower[rightIndex++];
                }
            }

            while (leftIndex < leftTowerSize) {
                leftTower[leftIndex].increaseDominanceBy(rightTowerSize - rightIndex);
                towers[mergeIndex++] = leftTower[leftIndex++];
            }

            while (rightIndex < rightTowerSize) {
                towers[mergeIndex++] = rightTower[rightIndex++];
            }

            // remove temporary left and right tower array
            delete[] leftTower;
            delete[] rightTower;
        }

        void findDominanceInLowerLeft(Tower *towers, int start, int end) {
            // State terminal condition
            if (start >= end - 1) return;

            // find mid-point index
            int mid = start + (end - start) / 2;

            // divide and conquer
            findDominanceInLowerLeft(towers, start, mid);
            findDominanceInLowerLeft(towers, mid, end);

            // create left and right temporary copied array
            int leftTowerSize = mid - start;
            int rightTowerSize = end - mid;

            auto *leftTower = new Tower[leftTowerSize];
            auto *rightTower = new Tower[rightTowerSize];

            int leftIndex = 0;
            int rightIndex = 0;
            for (int i = start; i < end; i++) {
                if (i < mid) {
                    leftTower[leftIndex++] = towers[i];
                } else {
                    rightTower[rightIndex++] = towers[i];
                }
            }

            // perform merging and find upper right dominance factor
            leftIndex = 0;
            rightIndex = 0;
            int mergeIndex = start;
            while (leftIndex < leftTowerSize && rightIndex < rightTowerSize) {
                if (leftTower[leftIndex].getX() > rightTower[rightIndex].getX()) {
                    leftTower[leftIndex].increaseDominanceBy(rightTowerSize - rightIndex);
                    towers[mergeIndex++] = leftTower[leftIndex++];
                } else {
                    towers[mergeIndex++] = rightTower[rightIndex++];
                }
            }

            while (leftIndex < leftTowerSize) {
                leftTower[leftIndex].increaseDominanceBy(rightTowerSize - rightIndex);
                towers[mergeIndex++] = leftTower[leftIndex++];
            }

            while (rightIndex < rightTowerSize) {
                towers[mergeIndex++] = rightTower[rightIndex++];
            }

            // remove temporary left and right tower array
            delete[] leftTower;
            delete[] rightTower;
        }
    }

    void findDominance(Tower *towers, int towers_size) {
        // reset dominance of every tower to 0
        for (int i = 0; i < towers_size; i++) {
            towers[i].setDominance(0);
        }

        // sort towers by their x coordinates in incremental order
        std::sort(towers, towers + towers_size, [](const Tower &t1, const Tower &t2) {
            return t1.getX() < t2.getX();
        });

        // find dominance factors for upper right corner of each towers
        helper::findDominanceInUpperRight(towers, 0, towers_size);

        // sort towers by their y coordinates in decremental order
        std::sort(towers, towers + towers_size, [](const Tower &t1, const Tower &t2) {
            return t1.getY() > t2.getY();
        });

        // find dominance factors for lower left corner of each towers
        helper::findDominanceInLowerLeft(towers, 0, towers_size);

        // sort towers by their ID in incremental order
        std::sort(towers, towers + towers_size, [](const Tower &t1, const Tower &t2) {
            return t1.getID() < t2.getID();
        });
    }
}

using CS341::PQ1::Tower;

int main(int argc, char *argv[]) {
    string line;
    getline(cin, line);

    int num_tower = std::stoi(line);
    auto *towers = new Tower[num_tower];

    for (int index = 0; index < num_tower; index++) {
        int id = 0;
        int x = 0;
        int y = 0;
        getline(cin, line);
        if (line.empty()) {
            index--;
            continue;
        }
        std::istringstream ss(line);
        ss >> id >> x >> y;
        towers[index] = Tower(id, x, y);
    }

    CS341::PQ1::findDominance(towers, num_tower);

    for (int i = 0; i < num_tower; i++) {
        std::cout << towers[i] << std::endl;
    }

    delete[] towers;
    return 0;
}

#endif // __TOWER_H__