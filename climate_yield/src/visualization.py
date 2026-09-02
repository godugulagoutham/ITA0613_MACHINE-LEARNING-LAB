from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def make_plots(df,knn_val,lwr_val,scalability,model_metrics,outdir):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    plt.figure(figsize=(8,5)); plt.scatter(df["Annual_Rainfall"],df["Yield"],s=8,alpha=.35); plt.xlabel("Annual rainfall"); plt.ylabel("Yield"); plt.title("Rainfall vs Crop Yield"); plt.tight_layout(); plt.savefig(outdir/"01_rainfall_vs_yield.png",dpi=220); plt.close()
    crop=df.groupby("Crop",as_index=False)["Yield"].mean().sort_values("Yield"); plt.figure(figsize=(9,5)); plt.bar(crop.Crop,crop.Yield); plt.xlabel("Crop"); plt.ylabel("Mean yield"); plt.title("Average Yield by Crop"); plt.xticks(rotation=30,ha="right"); plt.tight_layout(); plt.savefig(outdir/"02_average_yield_by_crop.png",dpi=220); plt.close()
    trend=df.groupby("Crop_Year",as_index=False)["Yield"].mean(); plt.figure(figsize=(8,5)); plt.plot(trend.Crop_Year,trend.Yield,marker="o",markersize=3); plt.xlabel("Year"); plt.ylabel("Mean yield"); plt.title("Yield Trend Over Time"); plt.tight_layout(); plt.savefig(outdir/"03_yield_trend.png",dpi=220); plt.close()
    cols=["Annual_Rainfall","Temperature","Humidity","Soil_pH","N","P","K","Fertilizer","Pesticide","GDD","Rainfall_Anomaly","Yield"]; c=df[cols].corr(); plt.figure(figsize=(9,7)); plt.imshow(c.values,aspect="auto"); plt.colorbar(label="Correlation"); plt.xticks(range(len(c.columns)),c.columns,rotation=60,ha="right",fontsize=8); plt.yticks(range(len(c.index)),c.index,fontsize=8); plt.title("Feature Correlation Matrix"); plt.tight_layout(); plt.savefig(outdir/"04_feature_correlation.png",dpi=220); plt.close()
    plt.figure(figsize=(7,5)); plt.plot(knn_val.k,knn_val.RMSE,marker="o"); plt.xlabel("k"); plt.ylabel("Validation RMSE"); plt.title("Manual kNN Validation Curve"); plt.tight_layout(); plt.savefig(outdir/"05_knn_validation_curve.png",dpi=220); plt.close()
    plt.figure(figsize=(7,5)); plt.plot(lwr_val.tau,lwr_val.RMSE,marker="o"); plt.xlabel("tau"); plt.ylabel("Validation RMSE"); plt.title("LWR Validation Curve"); plt.tight_layout(); plt.savefig(outdir/"06_lwr_validation_curve.png",dpi=220); plt.close()
    plt.figure(figsize=(7,5)); plt.plot(scalability.N,scalability.seconds,marker="o"); plt.xscale("log"); plt.yscale("log"); plt.xlabel("Records (log scale)"); plt.ylabel("Query time (s, log scale)"); plt.title("Brute-Force kNN Scalability"); plt.tight_layout(); plt.savefig(outdir/"07_scalability.png",dpi=220); plt.close()
    mm=pd.DataFrame(model_metrics); plt.figure(figsize=(7,5)); plt.bar(mm.Model,mm.RMSE); plt.ylabel("Test RMSE"); plt.title("Model Test RMSE Comparison"); plt.xticks(rotation=20); plt.tight_layout(); plt.savefig(outdir/"08_model_comparison.png",dpi=220); plt.close()
