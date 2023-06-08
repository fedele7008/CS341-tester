# Compiler
CXX := g++
CXXFLAGS := -std=c++17 -Werror=vla -Wall -MMD

# Source files
SRCS := towers.cpp

# Object files
OBJS := $(SRCS:.cpp=.o)

# Dependency files
DEPS := $(SRCS:.cpp=.d)

# Executable name
TARGET := towers

# Default target
all: $(TARGET)

# Build target
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(TARGET)

# Object file targets
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean target
clean:
	rm -f $(OBJS) $(DEPS)

# Clean all
clean-all:
	rm -f $(OBJS) $(DEPS) $(TARGET)
