# Correspondence analysis of 118 digital collections of scientific heritage
#
# Part of: Alina Volynskaya, Digital Archives of Science: Revisiting the
# Vestiges of Knowledge-Making (De Gruyter Oldenbourg, 2026).
# Data: https://doi.org/10.5281/ZENODO.16411455
#
# Input: CA.csv, a presence/absence matrix (1/0). Each row is a digital
# collection; each column is a way in which the collection organises and
# contextualises its items:
#   Links between items, subjects, across collections, dates, format,
#   actors, location/holdings, additional dimensions, interaction
#
# The analysis maps which modes of organisation tend to occur together and
# which collections resemble one another in how they present their objects.

library(FactoMineR)   # correspondence analysis
library(factoextra)   # plots
library(ggrepel)      # non-overlapping labels

# --- Load data ---------------------------------------------------------------

collections <- read.table(
  "CA.csv",
  header = TRUE, sep = ",", quote = "",
  row.names = 1, check.names = FALSE
)

stopifnot(sum(is.na(collections)) == 0)

# Collections with none of the features (row sum 0) cannot enter the
# analysis; CA() drops them automatically with a warning.
empty <- rownames(collections)[rowSums(collections) == 0]
if (length(empty) > 0) {
  message("Excluded (no features): ", paste(empty, collapse = "; "))
}

# --- Correspondence analysis -------------------------------------------------

res.ca <- CA(collections, graph = FALSE)
summary(res.ca)            # eigenvalues, contributions, cos2

# --- Plots -------------------------------------------------------------------

options(ggrepel.max.overlaps = 15)

# Scree plot: share of variance per dimension
fviz_screeplot(res.ca, addlabels = TRUE)

# Biplot of collections (rows) and features (columns)
fviz_ca_biplot(res.ca, repel = TRUE)

# Features only, the most readable view of the structure
fviz_ca_col(res.ca, repel = TRUE)

# Collections coloured by their contribution to the first two dimensions
fviz_ca_row(res.ca, col.row = "contrib", repel = TRUE) +
  scale_color_gradient2(low = "white", mid = "blue", high = "red", midpoint = 4)
